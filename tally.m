%This function tallies the amout of votes and returns the value that has the most.

function out = tally(mat)
  [value, index] = max(mat,[],2);
  
  index(find(value==0)) = size(mat)(2)+1;
  out = index;
  return
endfunction

%!test
%! A = [1,2,3;
%!     2,1,3;
%!     2,3,1;
%!     3,1,2;
%!     3,2,1;
%!     0,0,0];
%! assert (tally(A) == [3;3;2;1;1;4]);