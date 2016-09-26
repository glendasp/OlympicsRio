__author__ = 'Glenda Pinho'


"""
       Olympics 2016 Report
"""

class Sport(object):
    #Returns a Sport object with its name.
    def __init__(self, name):
        self.name = name

    def get_details(self):
        #Returns a string containing name of sport class
        return self.name


class Athlete(Sport):

    #Returns a Athlete object and takes 4 arguments: name, country, sport, medal.
    def __init__(self, name, country, sport, medal):
        Sport.__init__(self, name)
        self.country = country
        self.sport = sport
        self.medal = medal

    def get_details(self):
        #Returns a string containing athlete's details.
        return "%s %s competed in %s and won a %s medal." % (self.name, self.country, self.sport, self.medal)


class Country(Sport):

    #Returns a 'Country' object, takes a list of strings as argument.
    def __init__(self, name, medal):
        Sport.__init__(self, name)
        self.medal = medal

    def get_details(self):
        return "%s won %s" % (self.name, ','.join(self.medal))



"""

Few data to show how the report will be

"""

print("\n__ Rio 2015 __ \n")

sport1 = Sport('Track and field')
athlete1 = Athlete('-Tori Bowie', '(USA)', 'track and field', 'gold')
athlete2 = Athlete('-Simone Manuel', '(USA)', 'track and field', 'gold')
sport2 = Sport('Soccer')
athlete3 = Athlete('-Neymar', '(Brazil)', 'soccer', 'gold')

country1 = Country('USA', [' 46 Gold Medal', ' 37 Silver Medal', ' and 38 Bronse Medal'])
country2 = Country('Great Britain', [' 27 Gold Medal', ' 23 Silver Medal', ' and 17 Bronse Medal'])

print("*"+sport1.get_details())
print(athlete1.get_details())
print(athlete2.get_details())
print("\n*"+sport2.get_details())
print(athlete3.get_details())
print("\n"+country1.get_details())
print(country2.get_details())