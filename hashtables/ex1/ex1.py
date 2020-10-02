def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    # Loop through weights
    for index, weight in enumerate(weights):
        # store result of limit - weight and index
        cache[limit - weight] = index
        # loop again
    for index, i in enumerate(weights):
        # Check to see if result is in cache
        if i in cache:
            # Is index greater than i?
            if index > cache[i]:
                results = (index, cache[i])
                return results
            else:
                results = (cache[i], index)
                return results
        else:
            continue
    return None


# -> -> Time complexity should be O(n) <- <-

weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
get_indices_of_item_weights(weights_4, 9, 7)
