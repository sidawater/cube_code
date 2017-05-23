import random


def cube_scramble(step=20):
    layers = ['R', 'L', 'F', 'B', 'U', 'D']
    action = ['', '\'', '2']
    squences = []

    for i in range(step):
        def make_step():
            step = layers[random.randint(0,5)]
            if step_verify(step, squences):
                squences.append(step)
            else:
                make_step()
        make_step()

    aim_squences = [i + action[random.randint(0,2)] for i in squences]
    return ' '.join(aim_squences)


def step_verify(aim_step, squences=[]):
    varify_map = {
        'R': 'L',
        'L': 'R',
        'F': 'B',
        'B': 'F',
        'U': 'D',
        'D': 'U',
    }
    cross_map = {
        'R': 'FBDU',
        'L': 'FBDU',
        'F': 'RLDU',
        'B': 'RLDU',
        'U': 'RLFB',
        'D': 'RLFB',
    }

    if aim_step in squences or varify_map[aim_step] in squences:
        for step in squences[::-1]:
            d_mix = []
            if aim_step == step or varify_map[aim_step] == step:
                idx = squences.index(aim_step) if aim_step in squences else squences.index(varify_map[aim_step])
                d_mix = [i for i in squences[idx + 1:] if i in cross_map[aim_step]]
                break
        return len(d_mix) > 0
    else:
        return True


class MagicCube(object):

    '''
    确定配色方案:
        内置国际配色方案及日系配色方案
        手动配色方案默认为空, 须初始化时color_plan not in self.color_map, 并传入manual_color_plan参数

    确定初始方向:
        若配色方案为国际配色方案或日系配色方案, 须设置初始化方向, 须传入参数: up_color, front_color
        内置初始化方向为逆时针

    透视方法: 以front为基准, left在左边, up在上, down在下, right和back在右
    '''

    color_plan = 'international'
    color_map = {
        'international': {
            'U': 'white', 'D': 'yellow',
            'F': 'green', 'B': 'blue',
            'L':'orange', 'R': 'red'
        },
        'japanese': {
            'U': 'white', 'D': 'blue',
            'F': 'green', 'B': 'yellow',
            'L': 'orange', 'R': 'red'
        },
        'manual': {},
    }
    correct_direction = [
        'UFRU', 'URBU', 'UBLU', 'ULFU',
        'DRFD', 'DBRD', 'DLBD', 'DFLD'
    ]


    def __init__(self, up_color='white', front_color='green', color_plan='international', manual_plan={}):
        self.color_plan = color_plan
        if self.color_plan == 'manual':
            self.color_map['manual'] = manual_plan
            self.up = [self.color_map['manual'].get('U', 'white')for i in range(9)]
            self.down = [self.color_map['manual'].get('D', 'yellow')for i in range(9)]
            self.front = [self.color_map['manual'].get('F', 'green')for i in range(9)]
            self.back = [self.color_map['manual'].get('B', 'blue')for i in range(9)]
            self.left = [self.color_map['manual'].get('L', 'orange')for i in range(9)]
            self.right = [self.color_map['manual'].get('R', 'red')for i in range(9)]
        else:
            print(self.color_plan)
            self.up = [up_color for i in range(9)]
            self.front = [front_color for i in range(9)]
            self.right = [self.get_right_color(up_color, front_color) for i in range(9)]
            self.get_opposite_color()
            # self.down = ''
            # self.back = ''
            # self.left = ''

    def get_right_color(self, up_color, front_color):
        third_direction = ''
        r_color_map = {v: k for k, v in self.color_map.get(self.color_plan).items()}
        up_front = r_color_map.get(up_color, '') + r_color_map.get(front_color, '')

        for direction in self.correct_direction:
            if up_front in direction:
                third_direction = ''.join(set(direction) - set(up_front))
                right_color = self.color_map[self.color_plan][third_direction]
                break

        return right_color

    def get_opposite_color(self):
        # TODO: expect more PYTHONIC
        opposite_color_map = {
            'U': self.color_map.get(self.color_plan)['D'], 'D': self.color_map.get(self.color_plan)['U'],
            'F': self.color_map.get(self.color_plan)['B'], 'B': self.color_map.get(self.color_plan)['F'],
            'R': self.color_map.get(self.color_plan)['L'], 'L': self.color_map.get(self.color_plan)['R'],
        }
        opposite_color_map = {v: k for k, v in opposite_color_map.items()}

        if hasattr(self, 'up'):
            self.down = [self.color_map[self.color_plan][opposite_color_map[self.up[0]]] for i in range(9)]
        if hasattr(self, 'down'):
            self.up = [self.color_map[self.color_plan][opposite_color_map[self.down[0]]] for i in range(9)]
        if hasattr(self, 'front'):
            self.back = [self.color_map[self.color_plan][opposite_color_map[self.front[0]]] for i in range(9)]
        if hasattr(self, 'back'):
            self.front = [self.color_map[self.color_plan][opposite_color_map[self.back[0]]] for i in range(9)]
        if hasattr(self, 'right'):
            self.left = [self.color_map[self.color_plan][opposite_color_map[self.right[0]]] for i in range(9)]
        if hasattr(self, 'left'):
            self.right = [self.color_map[self.color_plan][opposite_color_map[self.left[0]]] for i in range(9)]

    @property
    def status(self):
        cube_status = {
            'up': self.up, 'down': self.down,
            'front': self.front, 'back': self.back,
            'left': self.left, 'right': self.right
        }
        return cube_status

    def move_step(self, step):
        base_change = {
            'clockwise_list': [6, 3, 0, 7, 4, 1, 8, 5, 2],
            'anticlockwise_list': [2, 5, 8, 1, 4, 7, 0, 3, 6],
            'double_list': [8, 7, 6, 5, 4, 3, 2, 1, 0],
        }
        change_map = {
            'R': {
                'neighbour': ['up', 'back', 'down', 'front', 'up'],
                'double_neighbour': ['up', 'down', 'front', 'back'],
                'change_neighbour': [2, 5, 8],
                'lower_change_neighbour': [1, 4, 7, 2, 5, 8],
            },
            'L': {
                'neighbour': ['up', 'back', 'down', 'front', 'up'],
                'double_neighbour': ['up', 'down', 'front', 'back'],
                'change_neighbour': [0, 3, 6],
                'lower_change_neighbour': [0, 3, 6, 1, 4, 7],
            }

        }
        if step == 'R':
            for i in change_neighbour:
                self.up[i], self.back[i], self.down[i], self.front[i] = (self.front[i], self.up[i],
                                                                         self.back[i], self.down[i])
            self.right = [self.right[i] for i in clockwise_list]

        # if step == 'F':
        #     self.up[6:], self.back[6:], self.down[6:], self.front[6:] = (self.front[6:], self.up[6:],
        #                                                                  self.back[6:], self.down[6:])
