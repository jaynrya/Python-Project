from tkinter import*
import time # import time for the progress bar
import socket
from pytube import YouTube, Search
import re
import datetime


# Youtube downloader app wtih a GUI


class main:

    

    def download():
        # Start download and print the progress in the user output
        text = mystring.get() # Get the string from the Entry box
        try:
            request = YouTube(text)
            request.streams.get_highest_resolution().download()

        except:
            displayOutput.insert(END, print('Error in connection') )

    
    def search():
    # Search and display top 5 result with their titles and links on the outbox
        text = mystring.get() # Get the string from the Entry box
        found_results = {}
        counter = 0
        request = Search(text)
        
        for v in request.results:
            if counter <= 5:
                found_results[v.title] = v.watch_url 
                counter += 1
        displayOutput.insert(END, [k for k in found_results.keys()for v in found_results.values()])
           
    # function for the window root
    def window(): 
        root = Tk()
        root.title("Kostbar Downloader App")
        root.geometry('380x550+480+90')
        root.resizable(0, 0)

        # insert text labels widget
        headLabel = Label(root, font=('Aerial 15 bold', 16),text="Download your YouTube Videos")
        headLabel.grid(row=1, column=0, columnspan=3, padx=10, pady=20, sticky = N + S + W + E)

        # insert text field Entry widget
        global mystring # make mystring global
        mystring = StringVar(root) # turning the input into a string

        txtIn = Entry(root, width=40, textvariable= mystring)
        txtIn.grid(row=2, column=0, columnspan=3)

        # Pop up dialog box widget
        #popUpBox = Message(root, text=popUp).pack()
        
        # Progess bar widget
        #progressBar = Progressbar(root, orient =HORIZONTAL,
                #length=200, mode= 'determinate')
        # Progress bar function
        #def bar():
            # progressBar['value'] = 20
            # root.update_idletasks()
            # time.sleep(1)

            # progressBar['value'] = 40
            # root.update_idletasks()
            # time.sleep(1)
  
            # progressBar['value'] = 50
            # root.update_idletasks()
            # time.sleep(1)
  
            # progressBar['value'] = 60
            # root.update_idletasks()
            # time.sleep(1)
  
            # progressBar['value'] = 80
            # root.update_idletasks()
            # time.sleep(1)
            # progressBar['value'] = 100
        
        #progressBar.grid(row=3, column=0, columnspan=1)

        # Download button
        
        downloadButton = Button(root, text="Download", width=8, command=main.download)
        downloadButton.grid(row=4, column=0, padx=0, pady=10)

        # Search button widget
        searchButton = Button(root, text="Search", width=8, command=main.search)
        searchButton.grid(row=4, column=1, padx=0, pady=10)

        # Exit application
        exitButton = Button(root, text="Quit",  width=8, command=root.destroy)
        exitButton.grid(row=4, column=2, padx=0, pady=10)

        # DisplayBox output
        global displayOutput
        displayOutput = Text(root, height=18, width=40)
        displayOutput.grid(row=5, column=0, columnspan=3, padx=10)

        # Generate PC name and IP Address
        hostname = socket.gethostname()   
        IPAddr = socket.gethostbyname(hostname)
        date = datetime.datetime.now() # current date 

        # Widget to display text
        displayHostname = Label(root, text="Computer name is: "+hostname, anchor='center')
        displayHostname.grid(row=6, column=0, columnspan=3,pady=5)
        displayIp = Label(root, text="Your Ip Address is: "+IPAddr)
        displayIp.grid(row=7, column=0, columnspan=3, pady=2)
        displayDate = Label(root, text="Date: "+ str(date))
        displayDate.grid(row=8, column=0, columnspan=3, pady=5)

        # Main loop to run the root 
        root.mainloop()

           

if __name__=="__main__":
    main.window()

# What we doing tomorrow
# download and searc section
# Display box fixing
#Additionl features
