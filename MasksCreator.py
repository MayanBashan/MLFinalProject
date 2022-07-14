from WeakKnnMask import WeakKnnMask

def create_position_mask(mapper):
    mask_fields = ["HomePos", "AwayPos"]
    headers = mapper.header_map
    mask_vec = [headers.index(val) for val in mask_fields]
    return WeakKnnMask("Position", mask_vec, mask_fields)

def create_points_mask(mapper):
    mask_fields = ["HomePts", "AwayPts"]
    headers = mapper.header_map
    mask_vec = [headers.index(val) for val in mask_fields]
    return WeakKnnMask("Points", mask_vec, mask_fields)


def create_odds_masks(mapper):
    masks = []
    for i in range(1, 6):
        mask_fields = []
        for result in ("H", "D", "A"):
            mask_fields.append(f"Odds{result}{i}")
        headers = mapper.header_map
        mask_vec = [headers.index(val) for val in mask_fields]
        masks.append(WeakKnnMask(f"Odds{i}", mask_vec, mask_fields))
    return masks


def create_rank_mask(mapper):
    mask_fields_total = []
    mask_vec = []
    for team in ("H", "A"):
        mask_fields = []
        for section in ("ATT", "MID", "DEF", "OVR"):
            mask_fields.append(f"{team}{section}")
        mask_fields_total.extend(mask_fields)
        headers = mapper.header_map
        mask_vec_temp = [headers.index(val) for val in mask_fields]
        mask_vec.extend(mask_vec_temp)
    return WeakKnnMask("Rank", mask_vec, mask_fields_total)


def create_players_value_mask(mapper):
    mask_fields = ["HPlayerValues", "APlayerValues"]
    headers = mapper.header_map
    mask_vec = [headers.index(val) for val in mask_fields]
    return WeakKnnMask("Players Values", mask_vec, mask_fields)

def create_market_value_mask(mapper):
    mask_fields = ["HMarketValue", "AMarketValue"]
    headers = mapper.header_map
    mask_vec = [headers.index(val) for val in mask_fields]
    return WeakKnnMask("Market Value", mask_vec, mask_fields)





def create_weak_knn_masks(mapper):
    weak_knn_masks = []
    weak_knn_masks.append(create_position_mask(mapper))
    weak_knn_masks.append(create_points_mask(mapper))
    weak_knn_masks.extend(create_odds_masks(mapper))
    weak_knn_masks.append(create_rank_mask(mapper))
    weak_knn_masks.append(create_players_value_mask(mapper))
    weak_knn_masks.append(create_market_value_mask(mapper))
    return weak_knn_masks
