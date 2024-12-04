import csv

def append_100( target_list ):
   target_list.append( 100 )

def main():
   tmp_list = [ 1, 2, 3, 4, 5 ]
   append_100( tmp_list )
   print( tmp_list )

if __name__ == "__main__":
    main()