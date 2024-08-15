import sqlite3
import datetime
class Db_manager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect('database/rps_base')
        self.cursor = self.connection.cursor()

    def create_game(self, computer, users, result):
        try:
            played_on = datetime.date.today()
            self.cursor.execute("INSERT INTO GAMES (computer, user,result,played_on) VALUES (?,?,?,?)",(computer, users, result[0], played_on))
            self.connection.commit()
        except Exception as e:
            print(e)
    
    def get_statistics(self):
        try:
            self.cursor.execute('select computer, count(*) from games group by computer')    
            count_by_computer = self.cursor.fetchall()
            self.cursor.execute("SELECT COUNT(*) FROM GAMES")
            games = self.cursor.fetchone()[0]
            self.cursor.execute("SELECT result, COUNT(*) FROM GAMES group by result")
            result = self.cursor.fetchall()
            self.cursor.execute("SELECT computer, COUNT(*) FROM GAMES where result= 'w' group by computer")
            won_by_selection = self.cursor.fetchall()
            self.cursor.execute("SELECT computer, COUNT(*) FROM GAMES where result= 't' group by computer")
            tie_by_selection = self.cursor.fetchall()
            self.cursor.execute("SELECT computer, COUNT(*) FROM GAMES where result= 'l' group by computer")
            lost_by_selection = self.cursor.fetchall()
            return {'total': {
                        'games': games, 
                        'won':result[2][1],
                        'tie':result[1][1],
                        'lost':result[0][1],
                        'p_won':(result[2][1]*100)/games,
                        'p_tie':(result[1][1]*100)/games,
                        'p_lost':(result[0][1]*100)/games
                    },
                    'played_rock': {
                        'total': count_by_computer[1][1],
                        'won': won_by_selection[1][1],
                        'tie': tie_by_selection[1][1],
                        'lost': lost_by_selection[1][1],
                        'p_won':(won_by_selection[1][1]*100)/count_by_computer[1][1],
                        'p_tie':(tie_by_selection[1][1]*100)/count_by_computer[1][1],
                        'p_lost':(lost_by_selection[1][1]*100)/count_by_computer[1][1]
                     },
                    'played_paper': {
                        'total': count_by_computer[0][1],
                        'won': won_by_selection[0][1],
                        'tie': tie_by_selection[0][1],
                        'lost': lost_by_selection[0][1],
                        'p_won':(won_by_selection[0][1]*100)/count_by_computer[0][1],
                        'p_tie':(tie_by_selection[0][1]*100)/count_by_computer[0][1],
                        'p_lost':(lost_by_selection[0][1]*100)/count_by_computer[0][1]
                     },
                     'played_scissors': {
                        'total': count_by_computer[2][1],
                        'won': won_by_selection[2][1],
                        'tie': tie_by_selection[2][1],
                        'lost': lost_by_selection[2][1],
                        'p_won':(won_by_selection[2][1]*100)/count_by_computer[2][1],
                        'p_tie':(tie_by_selection[2][1]*100)/count_by_computer[2][1],
                        'p_lost':(lost_by_selection[2][1]*100)/count_by_computer[2][1]
                     }
                    }

        except Exception as e:
            print(e)
