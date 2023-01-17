# iata_codes
A free dataset of the airline IATA codes made into a Python Class.

Instructions:
```
git clone https://github.com/elijaheaton/iata_codes.git
pip install beautifulsoup4
pip install lxml
```

And then in your Python code, include the following:
```
from iata_codes import Converter
converter = Converter()
converter.update()
print(converter.get_name('AA'))
```

In the end, that will print out American Airlines!
