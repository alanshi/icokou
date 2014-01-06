===================
 idea文档
===================

菜品搜索方案构思
========

菜品搜索类别
========

    1:菜品名
        1  food/search/?name=鱼香肉丝
        2  food/search/'name'='鱼香肉丝'
    2:菜品类别(家常菜,下酒菜,宴客等等)
        1  food/search/?type=家常菜
        2  food/search/'type'='家常菜'
    3:价格范围(1-10,10-15,15-30,30-100,100-200)
        1  food/search/?price=1,10
        2  food/search/price'='1-10'
    4:菜系(川菜,粤菜,鲁菜,湘菜)
        1  food/search/?class=川菜
        2  food/search/'class'='川菜'
    5:地域范围(系统内置的区域,顺庆区,高坪区,五星花园,和平路,金泉路等)
        1  food/search/?area=和平路
        2  food/search/'area'='和平路'
    6:口味(酸,甜,麻,辣)
        1  food/search/?taste=酸
        2  food/search/'taste'='酸'
        
        
    方案一: 除去菜品名 name=鱼香肉丝,参数需要用中文外,其他的均可用数据库内的id代替
    food/search/?name=鱼香肉丝&type=家常菜&price=1,10&class=川菜&area=和平路&taste=酸&isLike=like,isAnd=and
    好处在于传统拼接方式,简单
    缺点在于灵活度差,程序只能按照规定好的方式处理

    方案二:除去菜品名 name=鱼香肉丝,参数需要用中文外,其他的均可用数据库内的id代替
    food/search/'name'='鱼香肉丝','price'='1t10','class'='川菜','area'='和平路','taste'='酸','isLike'='like','isAND'='AND'
    
    好处在于灵活多变,程序能将其变成一个查询参数序列,自动化处理
    缺点在于过于过于复杂,用户看起来比较杂乱
    
    方案三:融合了1,2的特(目前方案)
    food/search/name=鱼香肉丝,price=1t10,class=川菜,area=和平路,taste=酸,isLike=like,isAND=AND
    
    方案四:未来
    
    food/search/鱼香肉丝,1至10元,川菜,和平路附近,酸

