class Random_fib:
    """
    class that generates random numbers
    """
    def __init__(self,amount_of_fib):
        self.current = 20
        self.l = [2, 6, 4, 9, 6]
        for x in range(amount_of_fib):
            self.fib_rng()

    def fib_rng(self,j=2,k=5):
        self.l.append((self.l[-j]+self.l[-k])%2**8)

    def random(self,max_fib = 1):
        self.current +=1
        return  (max_fib/255) * self.l[self.current]

class Season:
    def __init__(self):
        self.teams = []

    def add_teams(self,names,winning_chances):
        self.teams = names
        self.team_dict = {}
        for team in self.teams:
            self.team_dict[team] = 0
        # matrix with in each row the corresponding chances per other team
        self.winning_chances = winning_chances

    def start_season(self,fib):
        for team in self.teams:
            self.team_dict[team] = 0
        for row_i in range(len(self.winning_chances)):
            for i in range(len(self.winning_chances[0])):
                if row_i != i:
                    # print(self.teams[row_i]," is playing at home vs ", self.teams[i])
                    r = fib.random()
                    if r > self.winning_chances[row_i][i][0]:
                        if r >= self.winning_chances[row_i][i][0]+self.winning_chances[row_i][i][1]:
                            # team playing out wins
                            self.team_dict[self.teams[i]] +=3
                        else:
                            # tie
                            self.team_dict[self.teams[i]] +=1
                            self.team_dict[self.teams[row_i]] +=1
                    else:
                        #team playing home wins
                        self.team_dict[self.teams[row_i]] +=3

    def scores(self):
        return [i[0] for i in sorted(self.team_dict.items(), key= lambda key_value: (key_value[1], key_value[0]),reverse=True)]

        # return self.team_dict

def main():
    sim_len = 10000
    random_fib = Random_fib(21*sim_len)
    season = Season()
    season.add_teams(["Ajax","Feyenoord","PSV","FC Utrecht","Willem II"],
                     [[0,(.65,.17,.18),(.54,.21,.25),(.74,.14,.12),(.78,.13,.09)],
                      [(.3,.21,.49),0,(.37,.24,.39),(.51,.22,.27),(.6,.21,.19)],
                      [(.39,.22,.39),(.54,.22,.24),0,(.62,.20,.18),(.62,.22,.16)],
                      [(.25,.14,.61),(.37,.23,.4),(.29,.24,.47),0,(.52,.23,.25)],
                      [(.17,.18,.65),(.2,.26,.54),(.23,.24,.53),(.37,.25,.38),0]])
    score_lists = []
    for x in range(sim_len):
        season.start_season(random_fib)
        # print(season.scores())
        score_lists.append(season.scores())

    chances = [[],[],[],[],[]]
    for score_list in score_lists:
        for index in range(len(score_list)):
            chances[index].append(score_list[index])

    ajax = []
    feyenoord = []
    psv = []
    fc_utrecht = []
    willen_ii = []


    for places in chances:
        ajax.append(places.count("Ajax")/len(places))
        feyenoord.append(places.count("Feyenoord")/len(places))
        psv.append(places.count("PSV")/len(places))
        fc_utrecht.append(places.count("FC Utrecht")/len(places))
        willen_ii.append(places.count("Willem II")/len(places))

    print("                                          1e  2e  3e  4e  5e")
    print("Ajax win kansen zijn als volgt:      \t",[round(i*100) for i in ajax])
    print("Feyenoord win kansen zijn als volgt: \t",[round(i*100) for i in feyenoord])
    print("PSV win kansen zijn als volgt:       \t",[round(i*100) for i in psv])
    print("FC Utrecht win kansen zijn als volgt:\t",[round(i*100) for i in fc_utrecht])
    print("Willem II win kansen zijn als volgt: \t",[round(i*100) for i in willen_ii])


if __name__ == '__main__':
    main()



