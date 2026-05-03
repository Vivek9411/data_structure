# kmp theory
# kmp algo is used for pattern maching(optimized pattern matiching), it does this by pre calculating pattern that avoids repetative comparisions 

# so kmp also has two parts, first -> making pi table (performing some complutaitons and storing results ) 
# second -> the actual pattern machine, using this pi table 


# making/logic of pi table 
# pi table stores the lenght of the longest proper prefix which is also suffix for every prefix of the pettern (this can be confusing)
# think it of as a largest common part (in prefix and suffix (suffix is not equal to the complete string))

# so basically lingest proper prefix which is also suffix 


# now the code part

# function compute_pi(P):
#     n = length(P)
#     pi = array of size n
#     pi[0] = 0

#     j = 0   // length of current prefix-suffix

#     for i from 1 to n-1:
#         while j > 0 and P[i] != P[j]:
#             j = pi[j - 1]   // fallback

#         if P[i] == P[j]:
#             j = j + 1

#         pi[i] = j

#     return pi

#so the heart of the code is this in this inesead of falling back to the first position we go to the last best machine posistion to check if its equal to that we do till there is no prefix left to match with 
#     for i from 1 to n-1:
#         while j > 0 and P[i] != P[j]:
#             j = pi[j - 1]   // fallback


# the main logic suppose we have already matched preffix and suffix os lenth j till i 
# now we will complae i+1 index to j+1 index if they match good 
# if not then we will go back till j th index matched (using that emempt py table)
# this repeats until no lenth is left at all to match with 

def compute_pi(P):
    n = len(P)
    pi_table = [0]*n 
    matched_length = 0 

    for cur_index in range(1, n):
        while matched_length>0 and P[matched_length]!=P[cur_index]:
            matched_length = pi_table[matched_length-1]
        
        if P[matched_length] ==P[cur_index]:
            matched_length+=1 
        
        pi_table[cur_index] = matched_length
    return pi_table


def is_present(s, goal):
    pi_table = compute_pi(s)

    # now the machine part 
    # as we have the pi_table 
    n = len(s)
    j =0
    for idx in range(0, 2*n):
        i= idx%n
        while j>0 and goal[i]!=s[j]:
            j = pi_table[j-1]
        
        if goal[i]==s[j]:
            j+=1 
        
        if j==n:
            return True 
    return False