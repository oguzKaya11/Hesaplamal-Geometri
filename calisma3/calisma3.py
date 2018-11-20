# coding: utf-8

# In[13]:

def my_product(a, b):
    return a[0]*b[0] +  a[1]*b[1] + a[2]*b[2]    
def my_length_function(a):
    return my_product(a, a)**0.5
                


# In[21]:

def plane_point(plane, point):
    #draw plane
    #draw two point
    #print distance
    
    # d = ...
    # t = ...
    # p_0 = ...
    # plane,point,p_0
    
    plane_normal = [plane[0],plane[1],plane[2]]    
    d = my_product(plane,point)/my_length_function(plane_normal)
    
    t = -plane[3]-(my_product(plane_normal,point))
    t = t/my_product(plane_normal,plane_normal)
    
    p_0 = [0,0,0]
    p_0[0] = point[0]+t*plane[0]
    p_0[1] = point[1]+t*plane[1]
    p_0[2] = point[2]+t*plane[2]
    
    return d, t, p_0 # noktadan düzleme gitmek için gereken normal değer ...
    


# In[22]:

plane_1 = [1,2,3,-6]
point_1 = [4,2,10]
plane_point(plane_1,point_1) #d , plane ve point arasındaki uzaklık


# In[14]:

a = [1,2,3]
b = [4,5,6]
my_product(a, b), my_length_function(a), my_length_function(b)


# In[ ]:

# odev bunu çiz