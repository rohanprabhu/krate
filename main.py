from krate.krate import Krate

def main():
    Krate.do_something()
    
main()

class Film:
    def get_film_by_code(self, params):
        return "SELECT * FROM film WHERE code = {code}"
