class Utils:
    def printItemList(self,list):
       print(len(list))
       for alllist in list:
            print(alllist.text)

    # get the title that has 'searchinput' in it
    def assertListItemText(self,lists,textassert):
        for alltitles in lists:
            if textassert in alltitles.text:
                print("Titles that have " + textassert + " in it: ", alltitles.text)

    #get the title that doesnot have 'searchinput' in it
    def assertNotInListItemText(self,lists,textassert):
        for alltitles in lists:
            if textassert not in alltitles.text:
                print("Titles that doesnot have " + textassert+ " in it: ", alltitles.text)