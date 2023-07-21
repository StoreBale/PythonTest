story = [
    "You are lost in the jungle. You need to find a way out!",
    "You come across a river. Do you swim across or follow it?",
    "You see a glimmer of light in the distance. It could be a village or something else...",
    "The path splits into two directions. Which do you choose?"
]

# Set up game loop variables 
game_over = False 
current_section = 0

while not game_over:
    
    # Print current story section  
    print(story[current_section])
    
    if current_section == 0:
        # Get player input  
        choice = input("What do you want to do? (swim/follow)")
        
        if choice == 'swim':
            story.append("You made it across but your clothes are soaking wet.")
            
        elif choice == 'follow':
            story.append("After following the river for an hour, you come across an abandoned boat.")
        
        current_section += 1
        
    elif current_section == 1:
        # Get player input  
        choice = input("What do you want to investigate? (village/unknown)")

        if choice == 'village':
            story.append("As you approach the village, several people emerge from their homes and greet you warmly.")

        elif choice == 'unknown':
            story.append("As you get closer, the light disappears and all that remains is darkness.")
        
        game_over=True 
            
            
            
    
    
            
        
   
