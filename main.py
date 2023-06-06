import time
import os

message = ']\x8a\x89\x85\x8a\x90\x8d;\x88\x80\x8e;\x8f\x8dă\x8e;~\x83\x80\x8d\x8e;|\x8b\x8b\x8d\x80\x89|\x89\x8f\x8eI;aĄ\x87\x84~\x84\x8f|\x8f\x84\x8a\x89\x8e;û;\x91\x8a\x90\x8eG;\x91\x8a\x90\x8e;|\x91\x80\x95;\x8dĄ\x90\x8e\x8e\x84;û;~|\x8e\x8e\x80\x8d;~\x80;~\x8a\x7f\x80;<;e\x80;\x8e\x90\x84\x8e;\x81\x84\x80\x8d;\x7f\x80;\x91\x8a\x90\x8eI;h|\x84\x89\x8f\x80\x89|\x89\x8fG;\x91\x8a\x90\x8e;\x8b\x8a\x90\x91\x80\x95;~\x8a\x88\x88\x80\x89~\x80\x8d;\x87\x80;~\x8a\x7f\x80;\x7f\x80;q\x84\x82\x80\x89ă\x8d\x80'

the_key = 3

def brut_force():
    txt = split_message(message)
    for i in range(0, 100):
        # chiffre = chiffre_message(txt, i)
        dechiffre = reconstitution_message(txt, i)
        time.sleep(0.3)
        os.system('clear')
        print(i)
        print(dechiffre)



def split_message(mess):
    text_split = list(mess)
    return text_split

def chiffre_message(mess, cle = 2):
    temp = []
    for i in range(len(mess)):
        temp.append(chr(ord(mess[i]) + cle))
        resultat = "".join(temp)
    return resultat

def reconstitution_message(mess, cle = 2):
    mess_dechiffrer = []
    for i in range(len(mess)):
        mess_dechiffrer.append(chr(ord(mess[i]) - cle))
        resultat = "".join(mess_dechiffrer)
    return resultat
        

print(brut_force())