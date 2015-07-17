# JSONLibconfig
:sparkles: Pure python implementation library provides JSON <- convert -> Libconfig

## Install
```
pip install jsonlibconfig
```

## CLI Usage
```sh
λ ~/jsonlibconfig -h
usage: jsonlibconfig [-h] [--target {json,libconfig}] [--pretty] [--hextoint]
                     [--file FILE]

Pure python library provides JSON <- convert --> Libconfig

optional arguments:
  -h, --help            show this help message and exit
  --target {json,libconfig}
                        specify output format: json, libconfig (default:
                        libconfig)
  --pretty              Pretty print
  --hextoint            Convert HEX string to integer (only for json)
  --file FILE           Input file
```

**JSON to Libconfig**
```sh
cat example.cfg | jsonlibconfig --target json
```

    {"hours": {"mon": {"close": 18, "open": 9}, "wed": {"close": 18, "open": 9}, "sun": {"close": 16, "open": 11}, "fri": {"close": 20, "open": 9}, "sat": {"close": 20, "open": 9}, "thu": {"close": 18, "open": 9}, "tue": {"close": 18, "open": 9}}, "name": "Books, Movies & More", "inventory": {"movies": [{"media": "DVD", "price": 19.99, "qty": 11, "title": "Brazil"}, {"media": "DVD", "price": 18.99, "qty": 5, "title": "The City of Lost Children"}, {"media": "Blu-Ray", "price": 24.99, "qty": 20, "title": "Memento"}, {"title": "Howard the Duck"}], "books": [{"price": 29.99, "author": "Robert Louis Stevenson", "qty": 5, "title": "Treasure Island"}, {"price": 9.99, "author": "Neal Stephenson", "qty": 8, "title": "Snow Crash"}]}}

**Libconfig to JSON**
```sh
cat example.json | jsonlibconfig --pretty
```

      hours = {
        wed = {
          close = 18; 
          open = 9; 
        }; 
        sun = {
          close = 16; 
          open = 11; 
        }; 
        fri = {
          close = 20; 
          open = 9; 
        }; 
        tue = {
          close = 18; 
          open = 9; 
        }; 
        mon = {
          close = 18; 
          open = 9; 
        }; 
        thu = {
          close = 18; 
          open = 9; 
        }; 
        sat = {
          close = 20; 
          open = 9; 
        }; 
      }; 
      name = "Books, Movies & More"; 
      inventory = {
        movies = (
          {
            media = "DVD"; 
            price = 19.99; 
            title = "Brazil"; 
            qty = 11; 
          }, 
          {
            media = "DVD"; 
            price = 18.99; 
            title = "The City of Lost Children"; 
            qty = 5; 
          }, 
          {
            media = "Blu-Ray"; 
            price = 24.99; 
            title = "Memento"; 
            qty = 20; 
          }, 
          {
            title = "Howard the Duck"; 
          }
        ); 
        books = (
          {
            title = "Treasure Island"; 
            price = 29.99; 
            qty = 5; 
            author = "Robert Louis Stevenson"; 
          }, 
          {
            title = "Snow Crash"; 
            price = 9.99; 
            qty = 8; 
            author = "Neal Stephenson"; 
          }
        ); 
      }; 



## API
```python
from jsonlibconfig import encoder
from jsonlibconfig import decoder
```

**from json to libconfig**
```python
encoder.dumps(json.loads(inputs))
```

**from libconfig to json**
```python
decoder.loads(inputs))
```

## License
[MIT](http://yulun.mit-license.org)
