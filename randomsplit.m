%This function randomly splits a matrix using randperm based on the ratio inserted

function [x,y] = randomsplit(data, ratio)
  split = size(data)(1) * ratio;
  
  rows = randperm(size(data)(1), split);
  fMatrix = data(rows, :);
  
  unusedData = data(rows,:) = [];
  bMatrix = data;
  
  x = fMatrix;
  y = bMatrix;
  return
  
endfunction

%! assert(randomsplit(zeros(10,1), 0.5) == [zeros(5,1),zeros(5,1)]

%!test
%! [foo,bar] = randomsplit(zeros(10,1), 0.7)
%! assert(foo == zeros(7,1))
%! assert(bar == zeros(3,1))

%!test
%! [foo,bar] = randomsplit(zeros(100,1), 0.7)
%! assert(foo == zeros(70,1))
%! assert(bar == zeros(30,1))
