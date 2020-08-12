class Maze:
    def __init__(self, nome_file):
        f = open(nome_file)
        data_grezzi = f.read()
        lines = data_grezzi.split('\n')[:-1]
        self.adjacents = {}
        self.height = len(lines)
        self.width = len(lines[0])
        for i in range(len(lines)):
            line = lines[i]
            for j in range(len(line)):
                adiacenti = []
                self.adjacents[(i,j)] = adiacenti
                if lines[i][j] == ' ':
                    if j-1 >= 0 and lines[i][j-1] == ' ':
                        adiacenti.append((i, j-1))
                    if j+1 < len(lines[i]) and lines[i][j+1] == ' ':
                        adiacenti.append((i, j+1))
                    if i-1 >= 0 and lines[i-1][j] == ' ':
                        adiacenti.append((i-1, j))
                    if i < len(lines)-1 and lines[i+1][j] == ' ':
                        adiacenti.append((i+1, j))

        self.directions = {}
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j] == ' ':
                    self.directions[(i, j)] = '?'
                    if j == 0:
                        self.directions[(i, j)] = 'W'
                    if j == len(lines[i]) - 1:
                        self.directions[(i, j)] = 'E'
                    if i == 0:
                        self.directions[(i, j)] = 'N'
                    if i == len(lines)-1:
                        self.directions[(i, j)] = 'S'

    def __str__(self):
        result = ''
        for i in range(self.height):
            for j in range(self.width):
                if (i, j) in self.directions:
                    result += f' {self.directions[(i, j)]} '
                else:
                    result += ' * '
            result += '\n'
        return result

    def help(self):
        done = False
        while not done:
            done = True
            for corridor in self.directions:
                if self.directions[corridor] == '?':
                    adjacents_positions = self.adjacents[corridor]
                    for position in adjacents_positions:
                        if self.directions[position] != '?':
                            if corridor[0] == position[0] + 1:
                                self.directions[corridor] = 'N'
                            if corridor[0] == position[0] - 1:
                                self.directions[corridor] = 'S'
                            if corridor[1] == position[1] - 1:
                                self.directions[corridor] = 'W'
                            if corridor[1] == position[1] + 1:
                                self.directions[corridor] = 'E'
                            done = False
                            break



def main():
    maze = Maze('data.txt')
    maze.help()
    print(maze)

if __name__ == '__main__':
    main()
