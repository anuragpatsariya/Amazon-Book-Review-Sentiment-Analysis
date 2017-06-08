import Tkinter
import sys, os
import tkFileDialog as filedialog

if __name__ == '__main__':
    form = Tkinter.Tk()

    pathvalue = Tkinter.StringVar() #variable
    with open("file.txt", "a") as f:
            f.seek(0)
            f.truncate()

    
    def browsefunc():
        filename = filedialog.askopenfilename()
        pathEntry.config(text=filename)
        pathvalue.set(filename)

    def save():
        text = pathvalue.get() + "\n"
        with open("file.txt", "a") as f:
            f.write(text)
            pathEntry.config(text="")

    def reset():
        with open("file.txt", "a") as f:
            f.seek(0)
            f.truncate()

    def migrate():
        os.system('python F:\\amazon_book_reviews\\read_and_store_data.py')

    def execAnalysis():
        os.system('python F:\\amazon_book_reviews\\rating_and_sentiment.py')

    def sentimentcalc():
        os.system('python F:\\amazon_book_reviews\\positive_negative_sentiment_chart.py')
        
    def ratingcalc():
        os.system('python F:\\amazon_book_reviews\\Piechart.py')
        
    def senti_ratcalc():
        os.system('python F:\\amazon_book_reviews\\new_rating_sentiment.py')

    getFld = Tkinter.IntVar()

    form.wm_title('Amazon Book Review Sentiment Analysis')

    stepOne = Tkinter.LabelFrame(form, text=" 1. Select Movies: ")
    stepOne.grid(row=0, columnspan=7, sticky='W', \
                 padx=5, pady=5, ipadx=5, ipady=5)

    #Calculate Results #4
    helpLf = Tkinter.LabelFrame(form, text=" 4. Calculate Results ")
    helpLf.grid(row=0, column=9, columnspan=2, rowspan=8, \
                sticky='NS', padx=5, pady=5)
    sentiment = Tkinter.Button(helpLf, text=" Sentiment ",command=sentimentcalc)
    sentiment.grid(row=0,sticky='E', padx=5, pady=2)

    rating=Tkinter.Button(helpLf, text=" Rating ", width=9,command=ratingcalc)
    rating.grid(row=1,sticky='E', padx=5, pady=2)

    ratsent=Tkinter.Button(helpLf, text=" Rating & Sentiment ",command=senti_ratcalc)
    ratsent.grid(row=2,sticky='E', padx=5, pady=2)

    stepTwo = Tkinter.LabelFrame(form, text=" 2. Migrate to DB: ")
    stepTwo.grid(row=2, columnspan=7, sticky='W', \
                 padx=5, pady=5, ipadx=5, ipady=5)

    stepThree = Tkinter.LabelFrame(form, text=" 3. Execute Analysis: ")
    stepThree.grid(row=3, columnspan=7, sticky='W', \
                   padx=5, pady=5, ipadx=5, ipady=5)

    fileLbl = Tkinter.Label(stepOne, text="Select the File:")
    fileLbl.grid(row=0, column=0, sticky='E', padx=5, pady=2)

    pathEntry = Tkinter.Label(stepOne)
    pathEntry.grid(row=0, column=1, columnspan=7, sticky="WE", pady=3)

    browse = Tkinter.Button(stepOne, text="Browse file to migrate",command=browsefunc)
    browse.grid(row=0, column=8, sticky='W', padx=5, pady=2)

    savebutton = Tkinter.Button(stepOne, text="Save",width=9,command=save)
    savebutton.grid(row=2, column=1, sticky='E', pady=2)

    outEncLbl = Tkinter.Label(stepOne, text="              ")
    outEncLbl.grid(row=2, column=5, padx=5, pady=2)

    resetbutton = Tkinter.Button(stepOne,text="Reset",width=9,command=reset)
    resetbutton.grid(row=2, column=7, pady=2)


    #migrate button
    migrate = Tkinter.Button(stepTwo,text="Migrate to DB", width=20,command=migrate)
    migrate.grid(row=5, columnspan=5, padx=5, pady=2, sticky='WE')


    #executee analysis
    execute = Tkinter.Button(stepThree,text="Execute Analysis", width=20,command=execAnalysis)
    execute.grid(row=6, column=4, sticky='WE')

    form.mainloop()
