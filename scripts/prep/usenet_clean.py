#!/usr/bin/env python3

import sys, os, zipfile, time, glob, shutil, re, pickle
import urlextract
extractor = urlextract.URLExtract()

def get_mbox(file_list, slurm_job_id, slurm_task_id):
    extract_directory = os.path.join("/dev/shm", str(slurm_job_id), str(slurm_task_id))
    with open(file_list) as f:
        file_lines = f.readlines()
    usenet_zip_file_name = file_lines[slurm_task_id].rstrip()
    usenet_zip = glob.glob(os.path.join("**", usenet_zip_file_name), recursive = True)[0]
    with zipfile.ZipFile(usenet_zip, 'r') as f:
        f.extractall(extract_directory)
    with open(glob.glob(os.path.join(extract_directory, "*"))[0]) as f:
        usenet_file = f.read()
    shutil.rmtree(extract_directory, ignore_errors=True)
    return usenet_file

def get_messages(mbox):
    messages_temp = re.findall('(^From\s-?[0-9]+\n.+?)(^From\s-?[0-9]+\n|\Z)', mbox, flags = re.DOTALL | re.MULTILINE)
    messages = [m[0] for m in messages_temp]
    return messages

def encode(key, string):
    encoded_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = ''.join(encoded_chars)
    return encoded_string

def decode(key, string):
    encoded_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr((ord(string[i]) - ord(key_c) + 256) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = ''.join(encoded_chars)
    return encoded_string

def replace_url(string, dictionary):
    for key in dictionary:
        string=string.replace(key,dictionary[key])
    return string

def find_replace_url(string,replace=True,unlock=False):
    # findall() has been used  
    # with valid conditions for urls in string 
    #url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string) 
    url = extractor.find_urls(string)

    encrypt='usenet'
    
    if unlock:
        print("The key to decode the urls is: {}\nThis can be done with decode(key,string)\n".format(encrypt))
    
    urldict={}
    
    if len(url) > 0:
        for i in range(len(url)):
            urldict[url[i]]=encode(encrypt,url[i])
            
    #replace flag defaulted to true
    #if True, returns string with urls replaces
    #if False, returns a dictionary of {url,encoded url}
    
    if replace:
        output = replace_url(string,urldict)
    else:
        output = urldict
        
        
    return output

def header_to_dict(header, keylist=["Date","X-Google-Language",
                                    "Subject","Newsgroup","Organization"]):
    #Accepts header as string, splits along new lines,
    #searches resulting list of strings for keywords
    #and extracts them into python dictionary
    #Optional argument: keyword list
    headerdict={}
    headerlist = header.split("\n")
    for el in headerlist:
        for key in keylist:
            if key in el:
                headerdict[key]=el.split(": ")[-1]
    return headerdict

def check_lang(header_dictionary, lang="ENGLISH"):
    is_lang = True
    try:
        lang_str = header_dictionary["X-Google-Language"].lower()
    except KeyError:
        print("No language information, continuing")
        return is_lang
    if lang.lower() not in lang_str:
        is_lang = False
    return is_lang

def get_header_body(message):
    pattern = re.compile("(^From\s-?[0-9]+\n.+?\n\n)([\s\S]+)", flags = re.DOTALL | re.MULTILINE)
    header = pattern.findall(message)[0][0]
    body = pattern.findall(message)[0][1]
    return header, body

def remove_attachments(body):
    body = re.sub("^begin\s[0-7]{3,}[\s\S]+\n[\s\S]+`\nend", "", body)
    body = re.sub("^Content-Transfer-Encoding.+?", "", body, flags = re.DOTALL | re.MULTILINE)
    return body

def get_message_data(file_list, slurm_job_id, slurm_task_id):
    mbox = get_mbox(file_list, slurm_job_id, slurm_task_id)
    messages = get_messages(mbox)
    message_dicts = []
    for message in messages:
        header, body = get_header_body(message)
        header = "".join(header)
        message_dict = header_to_dict(header)
        if check_lang(message_dict):
            body = "".join(body)
            body = remove_attachments(body)
            body = find_replace_url(body)
            message_dict['Body'] = body
            message_dicts.append(message_dict)
    return message_dicts

def dump_data(data, file_name):
    with open(file_name, 'w+b') as f:
        pickle.dump(data, f)

def get_data(file_list, slurm_job_id, slurm_task_id, file_name):
    data = get_message_data(file_list, slurm_job_id, slurm_task_id)
    dump_data(data, file_name)

def main(file_list = "sub_newsgroups.txt", slurm_job_id = 314159,
         slurm_task_id = 1, file_name = "test.pickle"):
    get_data(file_list, slurm_job_id, slurm_task_id, file_name)

if __name__ == "__main__":
    try:
        file_list = sys.argv[1] 
        slurm_job_id = int(sys.argv[2])
        slurm_task_id = int(sys.argv[3])
        file_name = sys.argv[4]
        main(file_list, slurm_job_id, slurm_task_id, file_name)
    except:
        main()

