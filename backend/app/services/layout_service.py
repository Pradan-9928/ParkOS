from app.services.routing_service import shortest_path

def validate_layout(grid):
    entrances=[(r,c) for r,row in enumerate(grid) for c,x in enumerate(row) if x.get('type')=='entrance']
    exits=[(r,c) for r,row in enumerate(grid) for c,x in enumerate(row) if x.get('type')=='exit']
    slots=[(r,c) for r,row in enumerate(grid) for c,x in enumerate(row) if x.get('type')=='slot']
    errors=[]
    if not entrances: errors.append('At least one entrance is required')
    if not exits: errors.append('At least one exit is required')
    if not slots: errors.append('At least one parking bay is required')
    if entrances:
        for slot in slots:
            if not shortest_path(grid, entrances[0], slot): errors.append(f'No drivable path to slot at {slot[0]},{slot[1]}')
    return errors
