def Reward(self):
        """

        """
        try:
            # Entering Reward
            self.driver.find_element(
                By.ID, "mat-input-4").send_keys("Cash Rs1000/-")
            time.sleep(5)
            print("\n 18 - Entering Reward  ")

            self.ws['C11'] = 'Reward '
            self.ws['G11'] = 'Pass'
            self.wb.save(self.filename)

        except Exception as e:
            print("\n ERROR IN Reward  >>>>>>>>>>>>>>>\n\n")
            print(e)
            print("\n 18 - Unable to Add Reward ")

            self.ws['C11'] = 'Reward '
            self.ws['G11'] = 'Fail'
            self.wb.save(self.filename)