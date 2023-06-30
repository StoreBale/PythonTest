import random

# 定义迷宫地图
maze = [
    ["1", "1", "1", "1", "1", "1", "1"],
    ["1", "0", "0", "0", "0", "1", "1"],
    ["1", "0", "1", "1", "0", "0", "1"],
    ["1", "0", "0", "0", "1", "0", "1"],
    ["1", "0", "1", "0", "0", "0", "1"],
    ["1", "0", "0", "1", "0", "0", "1"],
    ["1", "1", "1", "1", "1", "1", "1"]
]

# 定义玩家位置
player_position = [1, 1]

# 定义终点位置
end_position = [5,5]
# 游戏循环
while True:
    # 打印迷宫地图
    for row_index,row in enumerate(maze):
        for cell_index,cell in enumerate(row):
            if row_index == player_position[0] and cell_index == player_position[1]:
                print('@', end=" ")
            elif row_index == end_position[0] and cell_index == end_position[1]:
                print('E', end=" ") 
            else:
                print(cell, end=" ")
        print()
        
    # 获取玩家输入
    move = input("请输入移动方向（wasd）：")
    
    # 更新玩家位置
    if move == "w":
        new_position = [player_position[0] - 1, player_position[1]]
    elif move == "a":
        new_position = [player_position[0], player_position[1] - 1]
    elif move == "s":
        new_position = [player_position[0] + 1, player_position[1]]
    elif move == "d":
        new_position = [player_position[0], player_position[1] + 1]
    else:
        print("无效的移动方向！")
        continue
    
    # 检查新位置是否合法
    if not (0 <= new_position[0] < len(maze) and 0 <= new_position[1] < len(maze[0])):
        print("超出边界！")
        continue
    elif maze[new_position[0]][new_position[1]] == "1":
        print("遇到1不能移动！")
        continue
    
    # 更新玩家位置
    player_position = new_position
    
    # 检查是否到达终点
    if player_position == end_position:
        print("恭喜你，闯关成功！")
        break
