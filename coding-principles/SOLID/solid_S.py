class Country:
    def __init__(self, name: str):
        self.name = name

class State:
    def __init__(self, name: str, country: Country):
        self.name = name
        self.country = country

class City:
    def __init__(self, name: str, state: State):
        self.name = name
        self.state = state

class Logger:
    @staticmethod # 
    def log(message: str):
        return f"Log: {message}"

# Example usage
countryOne = Country("Bangladesh")
stateOne = State("Dhaka Devision", countryOne)
cityOne = City("Dhaka", stateOne)
print(Logger.log(f"City: {cityOne.name}, State: {cityOne.state.name}, Country: {cityOne.state.country.name}"))

