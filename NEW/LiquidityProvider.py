import socket
import json
import sys
import rsa


def verify_client():
    #some way to verify whether its an authenticated client or not, if not then process for exchange will terminate and further actions will be taken :)
    pass

def exit_func():
    print("hmmmm")

def decrypt(ciphertext, key):
    try:
        return rsa.decrypt(ciphertext, key).decode('ascii')
    except:
        return False

def get_info(privKey):

    while 1:
        try:   
            data = conn.recv(1024)
            datastr = data.decode()
            # print(datastr)
            bytdata = bytes(datastr,encoding="ascii")
            resdata = bytdata.decode('unicode-escape').encode('ISO-8859-1')
            print(resdata)
            slicing_byte_1 = resdata[:-1]
            final_byte_data = slicing_byte_1[2:131]
            print(final_byte_data)
            print(len(final_byte_data))
            # print(privKey)
            print(type(final_byte_data))
            # print(type(privKey))
          
            res = decrypt(final_byte_data,privKey)
            print("decryption: " + str(res)) #res is 'False' for some reason
           
            if len(resdata) != 0:
                break
           
        except:
            # print("Waiting...")
            pass

    exit_func()
       
    

    

def send_pub_key(): #send public key to the client peer for encrypting the exchange info
    (pubKey, privKey) = rsa.newkeys(1024)   
    # print(sys.getsizeof(pubKey)) #Debugging
    public_key_str = pubKey.save_pkcs1().decode("utf-8") #Dont ask me how this works, took me an entire day to figure out conversion from string to RSA Public Class

    conn.sendall(public_key_str.encode())
   
    get_info(privKey)



   
#Program starts here
if __name__ ==  "__main__":
    #TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind(('localhost', 50002))

    Current_BTC_Rate = "100" #Hypothetical

    s.listen(1)
    conn, addr = s.accept()
    #Verify Client before allowing exchange info to be received
    verify_client()
    #Send public Key
    send_pub_key()
    
