# multidimensional list
float_lists = [[ 3.0, 2.0, 1.0 ],
                [ 3.0, 1.0, 2.0 ],
                [ 2.0, 3.0, 1.0 ],
                [ 2.0, 1.0, 3.0 ],
                [ 1.0, 3.0, 2.0 ],
                [ 1.0, 2.0, 3.0 ]]

for each_sublist in float_lists:
   each_sublist.sort()
   print( each_sublist )