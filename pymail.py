from email_validator import validate_email, EmailNotValidError
import argparse
import textwrap
from rich import print



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Validator of email address: ",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    epilog=textwrap.dedent("""Example:\n

    pymail.py -e <email> \n
    pymail.py -w <wordlist> #for use a wordlist of email to validate#\n
    pymail.py-o <outputfile> #Save the output into a text file#\n
    """))
    parser.add_argument('-e','--email',help="Insert an email")
    parser.add_argument('-w','--wordlist',help="Use a wordlist of email")
    parser.add_argument('-o','--output',help="Save the output into a file text")
    args = parser.parse_args()
    target = args.email
    wlist = args.wordlist
    out = args.output




try:
    if target:
        
        emailObject = validate_email(target)
       
        validate_mail = emailObject.email
        output =(f"{validate_mail}    ✓")
        print(f"[bold green]{output}")
    else:
        print("Please, insert an email")
        print("Use [-h] to show the help")   
except EmailNotValidError as errorMsg:
    print(f"[bold red]✗ {str(errorMsg)} ✗")

try:
    #if the user choose a wordlist then...
    if wlist:
        #analyze wordlist
        wordlistline = open(wlist,'r').readlines()
        for i in range(0,len(wordlistline)):
            #creating an output
            res = wordlistline[i].replace('\n','')
            #validating the email
            email_object= validate_email(res)
            valid_mail= email_object.email
            #print the result
            results = (f"{valid_mail}   ✓")
            print(f"[bold green]{results}")
            #if user choose output then save the output into a file text
            if out:                    
                f = open(out,'a')
                f.write(results+'\n')
                f.close()
             
except EmailNotValidError as errorMsg:
    pass
