class Utils:
    def assertTitle(self,titleinSearch, titleinCart):
        for list in titleinSearch:
            if titleinCart == list.text:
                print("The title in" +titleinCart+ "matches with", list.text)