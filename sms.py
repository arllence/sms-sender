import math
length = 160
max = 1440
sms = "As a reminder, you have an appointment with Dr. Smith tomorrow at 3:30 pm. If you are unable to make this appointment, please call our customer service line at least 1 hour before your scheduled appointment time."

len_sms = len(sms) 
  

def chunks_constructor(n,m,text_reconstruct,text_chunks):
    paging = "(" + str(n)+'/'+str(m) + ")"      
    text_reconstruct = (text_reconstruct + str(paging))
    text_chunks.append(text_reconstruct)

def main(sms,len_sms,length,max):

    if len_sms > length:
        text = sms # reassigns the sms to text variable; not necessary jst incase you dont want to alter sms
        text = text.split() # converts sms to a list of words
        text_chunks = [] # stores 160 characters splited text
        text_reconstruct = "" # store new str text of 160 characters

        n = 0 # indicates index of sms if splitted
        m = math.ceil(len_sms/length) # indicates the total number of sms chunks to be sent

        paging = "(" + str(n)+'/'+str(m) + ")"        
        len_paging = len(str(paging))

        count = 0 # ensures we don't surpass the 160 length
        max_count = 0  # indicates if maximum sms legnth is reached

        for i in text:
            i = i + ' ' # appends a space to the  word
            len_i = (len(i)) # finds the length of the word

            count += len_i
            max_count += len_i

            if count < (length - len_paging):
                text_reconstruct += i
                if max_count > len_sms:
                    n = n + 1 
                    chunks_constructor(n,m,text_reconstruct,text_chunks)
            else:
                n = n + 1 
                chunks_constructor(n,m,text_reconstruct,text_chunks)

                # reset variable
                text_reconstruct = ""
                text_reconstruct += i
                count = 0

        # printing results
        print("\nResulst: \n")
        for sms in text_chunks:
            print("Sending sms...\n", sms)
            print("\n")




# start processing
if len_sms > max:
    print(f"Text too long maximum is 1440 characters")
else:
    main(sms,len_sms,length,max) 