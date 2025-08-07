# ascii_art.py
# High-res (80x80) ASCII art for items and default Sword

ASCII_GUIDES = {
    '#': (r"""
""" + "#"*80 + "\n"*79, "Wall: Blocks your path. Find a way around!"),
    'T': (r"""
""" + "$"*80 + "\n"*79, "Treasure: Collect for rewards!"),
    'V': (r"""
""" + "V"*80 + "\n"*79, "Vendor: Trade treasures for potions."),
    'C': (r"""
""" + "C"*80 + "\n"*79, "Cave: Face a challenge for a reward!"),
    'M': (r"""
""" + "M"*80 + "\n"*79, "Monster: Fight or flee!"),
    'P': (r"""
""" + "P"*80 + "\n"*79, "Potion: Restores health when used."),
    'N': (r"""
""" + "N"*80 + "\n"*79, "NPC: Meet a mysterious character. Maybe they have a quest!")
}

DEFAULT_SWORD_ART = (r"""
                                                                      █         
                                                                   █████        
                                                                ████████        
                                                              ██████████        
                                                            ██████ ████         
                                                          ██████ █████          
                                                         ██████ ████            
                                                       ████████████             
                                                     ████ ████ ███              
                                                   ███████ ██████               
                                                  █████████ ███                 
                                                ████ ██ ██████                  
                                              ███████ ██ ████                   
                                             ████ █████████                     
                                           ████ ██ ██ ████                      
                                         ███████████████                        
                                        ████ ██ ██ ████                         
                                       █████████ ████                           
                                     ████ ██████████                            
                                   ██████████ ████                              
                                  ████ █████████                                
                                ████ ██ ██ ████                                 
                               ██████████████                                    
                             ████ ██ ███████                                    
                            █████████ ████                                      
                   ███    ████ █████████                                        
                  ████  ███████ ██ ████                                         
                   ██████████████████                                           
                   ██ ██████ ██ ████                                            
                    █████ ████████                                              
                   ████ █████████                                               
                   ██ ██████████████                                            
                  ██ █ ██████     ██                                            
               ███ ██   ████████████                                            
               █ █ ██ ██                                                        
             ██ █ █████                                                         
           ██████  ███                                                          
        ████████████                                                            
        ███ █████                                                               
        ████████                                                                
        ████████                                                                
          █████                                                                 
""" + "\n"*39, "The Sword: Your legendary weapon.")
