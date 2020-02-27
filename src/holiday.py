import requests

class Holidays:
    """
    @ref https://calendarific.com/api-documentation
    """
    @staticmethod
    def holidays_list_connection(iso_3166_country, year):

        params_for_holiday = {
            'api_key': 'a25c1263fb01f8bd99b79f15fd3265a9b4236850',
            'country': iso_3166_country,
            'year': year
        }

        api_results_holiday = requests.get("https://calendarific.com/api/v2/holidays",params_for_holiday)
        api_response_holiday = api_results_holiday.json()
        return api_response_holiday['response']['holidays']

    @staticmethod
    def list_country():
        params = {
            'api_key': 'a25c1263fb01f8bd99b79f15fd3265a9b4236850',
        }

        api_results = requests.get("https://calendarific.com/api/v2/countries", params)
        api_response = api_results.json()

        return api_response['response']['countries']

    @staticmethod
    def country_name_to_iso(country_name):
        countries = Holidays.list_country()

        for country in countries:
            if str(country['country_name']) == country_name:
                return country['iso-3166'], country['total_holidays']

        return -1, -1

    @staticmethod
    def print_holiday_list_name_and_date(country, year):
        iso_country, total_holidays = Holidays.country_name_to_iso(country)

        if iso_country == -1:
            print('The country you choose is not on the list or wrong writing')
            return

        results = Holidays.holidays_list_connection(iso_country,year)
        print("The total holidays'number of the {0} is: {1}".format(country,total_holidays))
        print("The " + country + " holidays:")
        for item in results:
            print('{0} - in date: {1}.{2}.{3}'.format(item['name'],item['date']['datetime']['day'],
                                                      item['date']['datetime']['month'],
                                                      item['date']['datetime']['year']))


if __name__ == '__main__':
    country = input("Enter a country:")
    year = input("Enter year: ")
    Holidays.print_holiday_list_name_and_date(country,year)