
from banana import Score



def main():
    
    new_record = Score("TMEP\mich.txt")

    s = 100
    new_record.set_score(s)
    
    s = s + 500

    new_record.set_score(s)

    print(new_record.get_score())
    


main()
