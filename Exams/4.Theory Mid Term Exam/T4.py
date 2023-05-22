space_invaders = [ ]
player_pos = ( 200 , 25 )
level = 1 
max_level = 10

def play():
    print('\n In play:, __name__: ', __name__)
    print('\t\t globals: ', [k for k in globals().keys() if not k.startswith('__')])
    print('\t\t locals; ', [k for k in locals().keys() if not k.startswith('__')])
    while ( level < max_level +1 ) :
         if len ( space_invaders ) == 0 : 
            level += 1 
            continue
    print('\t\t globals: ', [k for k in globals().keys() if not k.startswith('__')])
    print('\t\t locals; ', [k for k in locals().keys() if not k.startswith('__')])

    #return max_level
play()
#print(res)

print('\n At global scope, __name__: ', __name__)
print('\t globals: ', [k for k in globals().keys() if not k.startswith('__')])
print('\t locals; ', [k for k in locals().keys() if not k.startswith('__')])