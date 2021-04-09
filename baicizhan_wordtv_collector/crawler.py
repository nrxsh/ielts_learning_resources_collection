# Its fast to write with python , but its a pain to wating for your snail like program finish its task.
import requests
import os.path
class ScrapyBaicizhan():
    def __init__(self, base_url, word_list_path,out_dir):
        self.out_dir = out_dir
        self.base_url = base_url
        self.word_list_path = word_list_path

    def scrapy(self):
        with open(word_list_path, 'r') as f:
            words = f.readlines()
            count = 0
            index = 0
            for word in words:
                word = word.strip('\n')
                if self.word_exsits(word,out_dir):
                    continue
                urls = self.get_urls(word)
                for url in urls:
                    r = requests.get(url)
                    if r.status_code == 200:
                        index += 1
                        with open('%s/%s.mp4' % (out_dir,word), 'wb+') as f:
                            count += 1
                            print("collect %s words;progress: %.2f%%;word: %s" % (count,(index/len(words))*100,word))
                            f.write(r.content)
                        break
                    else:
                        continue
            # with open('count.txt', 'wa+') as f:
            #     f.write("collect %s videos of words" %count)

    def scan_files(self):
        postfix='.mp4'
        files_list=[]
        with open(out_dir+'\%s.txt'%self.out_dir, 'wb+') as f:
            for root, sub_dirs, files in os.walk(os.getcwd()+"\\"+self.out_dir):
                for special_file in files:
                    if postfix:
                        if special_file.endswith(postfix):
                            print(special_file.replace(postfix,''))
                            word = special_file.replace(postfix,'')
                            files_list.append(word)
                            f.write((word+"\n").encode())
                    
        return files_list
            

    def get_urls(self, word):
        return_list = []
        add_before = ["music", "noun", "real", "leng"]
        for i in add_before:
            return_list.append(self.base_url + i + '_' + word + '.mp4')
        return return_list
    
    def word_exsits(self, word,out_dir):
        return os.path.isfile(out_dir + "/" + word + '.mp4')

if __name__ == '__main__':
    base_url = "http://ali.baicizhan.com/word_tv/"
    print("all path is relative to the current directory");
    word_list_path = input("input the word list file (each words stands a line) path:")
    out_dir = input("input the output dir path:")
    scrapy = ScrapyBaicizhan(base_url, word_list_path,out_dir)
    # url = scrapy.get_urls("seek")
    # r = requests.get(url[-1])
    # print(r.content)
    # print(scrapy.word_exsits("hello"))
    scrapy.scrapy()
    print(scrapy.scan_files())
    # r=requests.get("http://ali.baicizhan.com/word_tv/leng_seek.mp4")
    # print(r.status_code)
