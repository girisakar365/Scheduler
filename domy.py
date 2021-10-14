from random import *


class DataGen:
    id_check = []

    def id_gen(f: str, s: str):
        if f[0] + s[0] not in DataGen.id_check:
            DataGen.id_check.append(f[0] + s[0])
            return f[0] + s[0]
        else:
            shortname = "".join(sample(f.replace(f[0], "") + s.replace(s[0], ""), 1))
            while shortname in DataGen.id_check:
                shortname = "".join(
                    sample(f.replace(f[0], "") + s.replace(s[0], ""), 1)
                )
            else:
                return f[0] + shortname + s[0]

    def gen_data(limit: int = 27):
        name = [
            "Uttam Raj",
            "Ram",
            "Shyam",
            "Hari",
            "Samip",
            "Varun",
            "Bardan",
            "Ashutosh",
            "Darwin",
            "Bikalpa",
            "Swostik",
            "Sanshkar",
            "Abiyan",
            "Dev",
            "Nagendra",
            "Bhola",
            "Rajesh",
            "Prakash",
            "Dash",
            "Rikesh",
            "Devendra",
            "Uttam",
            "Ankit",
            "Pratik",
            "Lexie",
            "Leslie",
            "Jill",
            "Eilen",
            "Jonathan",
            "Jane",
            "David",
            "Ann",
            "Sheila",
            "Simon",
        ]

        sname = [
            "Bhusal",
            "Arayal",
            "Galwali",
            "Arayal",
            "Ghimire",
            "Shrestha",
            "Ghimire",
            "Sharma",
            "Acharya",
            "Giri",
            "Nepal",
            "Kharel",
            "Kadel",
            "Barma",
            "Timalsina",
            "Poudle",
            "Panthi",
            "Tiwari",
            "Pudasini",
            "Niraula",
            "Maharjan",
            "Anderson",
            "Austin",
            "Baker",
            "Barlett",
            "Barrow",
            "Begum",
            "Blackmore",
            "Boughton",
            "Brown",
            "Burrell",
            "Carroll",
            "Chapman",
            "Cheung",
        ]

        data_lst = []

        for i in range(limit):
            shuffle(name)
            shuffle(sname)
            fristName = choice(name)
            secondName = choice(sname)
            email = fristName.lower().capitalize() + secondName.lower() + "@gmail.com"
            id = DataGen.id_gen(fristName.upper(), secondName.upper())
            subject = choice(
                [
                    "Physics",
                    "Chemistry",
                    "Maths",
                    "Computer",
                    "Biology",
                    "English",
                    "Nepali",
                ]
            )
            _class = choice(["11", "12", "both"])

            data_lst.append([fristName, secondName, id, subject, email, _class])

        return data_lst
