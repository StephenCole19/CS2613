
## Example to visualize the "buckets" discussed in assignment 6.

## there are 3 features (3 columns)
## you can change p and ranges
ranges = [0,1,3;
          1,2,9]
p=3

ranges(1,1)
ranges(1,3)

x = linspace(ranges(1,1),ranges(2,1),p+1)
y = linspace(ranges(1,2),ranges(2,2),p+1)
z = linspace(ranges(1,3),ranges(2,3),p+1)

[X,Y] = meshgrid(x,y)

clf
axis([ranges(1,1),ranges(2,1),ranges(1,2),ranges(2,2),ranges(1,3),ranges(2,3)],"equal")
hold on
for i=1:columns(z)
  surf(X,Y,ones(size(X))*z(i))
endfor
for i=1:columns(x)
  for j=1:columns(y)
    plot3(ones(size(z))*x(i),ones(size(z))*y(j),z)
  endfor
endfor
