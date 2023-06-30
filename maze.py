import random

maze = [
    ["1", "1", "1", "1", "1", "1", "1"],
    ["1", "0", "0", "0", "0", "1", "1"],
    ["1", "0", "1", "1", "0", "0", "1"],
    ["1", "0", "0", "0", "1", "0", "1"],
    ["1", "0", "1", "0", "0", "0", "1"],
    ["1", "0", "0", "1", "0", "0", "1"],
    ["1", "1", "1", "1", "1", "1", "1"]
]
#玩家開局位置
player_position = [1, 1]
#迷宮出口位置
end_position = [5,5]

while True:
    
    for row_index,row in enumerate(maze):
        for cell_index,cell in enumerate(row):
            if row_index == player_position[0] and cell_index == player_position[1]:
                print('@', end=" ")
            elif row_index == end_position[0] and cell_index == end_position[1]:
                print('E', end=" ") 
            else:
                print(cell, end=" ")
        print()
        
    
    move = input("請輸入移動方向（wasd）：")
    
    
    if move == "w":
        new_position = [player_position[0] - 1, player_position[1]]
    elif move == "a":
        new_position = [player_position[0], player_position[1] - 1]
    elif move == "s":
        new_position = [player_position[0] + 1, player_position[1]]
    elif move == "d":
        new_position = [player_position[0], player_position[1] + 1]
    else:
        print("請使用正確方向鍵！")
        continue
    
    
    if not (0 <= new_position[0] < len(maze) and 0 <= new_position[1] < len(maze[0])):
        print("超過地圖！")
        continue
    elif maze[new_position[0]][new_position[1]] == "1":
        print("撞牆了！")
        continue
    
    player_position = new_position
    
    if player_position == end_position:
        print("恭喜你，成功！")
        break
