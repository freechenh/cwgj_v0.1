#/usr/bin/python
#encoding:utf-8


from Crypto.Cipher import AES
import base64


class AESECB:

    block_size = 16

    @staticmethod
    def encrpyt(content,tk):
        byte_content = content.encode('utf-8')
        byte_key = tk.encode('utf-8')[0:16]
        aes_new = AES.new(byte_key)
        if AESECB.block_size > len(byte_content):
            padding = AESECB.block_size - len(byte_content)
            byte_content = byte_content + chr(padding).encode('utf-8')*padding
        elif AESECB.block_size < len(byte_content):
            padding = AESECB.block_size - (len(byte_content)%AESECB.block_size)
            byte_content = byte_content + chr(padding).encode('utf-8') * padding
        else:
            byte_content = byte_content + chr(16).encode('utf-8') * 16
        result = aes_new.encrypt(byte_content)
        base_result = base64.b64encode(result).decode('utf-8').replace('\n','').replace('\r','')
        return base_result

    @staticmethod
    def decrpyt(encontent,tk):
        key = tk[0:16]
        des_new = AES.new(key)
        decrpytBytes = base64.b64decode(encontent)
        #str_encontent = str(decrpytBytes)
        #str_encontent += (len(str_encontent) % 4) * '='
        #print(decrpytBytes)[
        #print(len(decrpytBytes))
        meg = des_new.decrypt(decrpytBytes)
        return meg.decode('utf-8').strip('')




# content = b'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'
# tk = '0D8DF03BDAD8B96274A86EA6BE502E2B'
#
# a = AESECB.decrpyt(content,tk)
# print(a)