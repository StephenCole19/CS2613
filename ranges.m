%This function finds the min and max values in the matrix

function ret = ranges(data)

  ret = [min(data);max(data)];
  return
  
endfunction

%!test
%! A = [0,0,0;
%!          0,1,0;
%!          0,0,1;
%!          1,1,1];
%! assert (ranges(A), [0,0,0;
%!                     1,1,1]);

%!test
%! A=[0,0,0;
%!    0,10,0;
%!    0,0,1;
%!    1,1,-11];
%! assert (ranges(A), [0,0,-11;
%!                     1,10,1]);

%!test
%! A = [0,5.1,0;
%!          0,1,0;
%!          0,0,1;
%!          1,1,1];
%! assert (ranges(A), [0,0,0;
%!                     1,5.1,1]);