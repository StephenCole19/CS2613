%This function returns a vector containing the same amount of dimensions as the ranges passed in
%This vector will be which bucket the value pertains to

function out = bucket(point, ranges, p)
  %bucket sizes of each dimension
  diffs = [(ranges(2,2:end)-ranges(1,2:end))/p];

  %subtract the lower range from the point  and divide each value
  %by the bucket size for that dimension.
  div = floor((point(2:end).-ranges(1,2:end))./diffs);
  
  %forcing edge values into bucket p-1
  maxvalues = find(div>=p);
  div(maxvalues)  = p - 1;
  
  %forcing values outside of the range into bucket 0
  minvalues = find(div<0);
  div(minvalues) = 0;
  
  out = div;
endfunction
%!test "[*,0] -> bucket 0"
%!shared zero_one
%! zero_one=[0,0;1,1];
%! assert(bucket([0,0],zero_one,2) == 0)
%! assert(bucket([1,0],zero_one,2) == 0)

%!test "[*,0.1] -> bucket 0"
%!shared zero_one
%! zero_one=[0,0;1,1];
%! assert(bucket([0,0.1],zero_one,2) == 0)
%! assert(bucket([1,0.1],zero_one,2) == 0)

%!test "[*,0.5] -> bucket 1"
%! assert(bucket([0,0.5],zero_one,2) == 1)
%! assert(bucket([1,0.5],zero_one,2) == 1)

%!test "[*,0.6] -> bucket 1"
%! assert(bucket([0,0.6],zero_one,2) == 1)
%! assert(bucket([1,0.6],zero_one,2) == 1)

%!test "[*,1] -> bucket 1"
%! assert(bucket([0,1],zero_one,2) == 1)
%! assert(bucket([1,1],zero_one,2) == 1)

%!test "[*,1] p=3 -> bucket 2"
%! assert(bucket([0,1],zero_one,3) == 2)
%! assert(bucket([1,1],zero_one,3) == 2)

%!test "[*,1] (range=1,2) -> bucket 0"
%!shared one_two
%! one_two=[1,1;2,2];
%! assert(bucket([0,1],one_two,2) == 0)
%! assert(bucket([1,1],one_two,2) == 0)

%!test "[*,1.5] (range=1,2, p=3) -> bucket 1"
%! assert(bucket([0,1.5],one_two,3) == 1)
%! assert(bucket([1,1.5],one_two,3) == 1)

%!test "d=2, p=2, [*,0,0] -> [0,0]"
%!shared zero_one2
%! zero_one2=[0,0,0;1,1,1];
%! assert(bucket([0,0,0],zero_one2,2) == [0,0])
%! assert(bucket([1,0,0],zero_one2,2) == [0,0])

%!test "d=2, p=2, [*,0.6,0] -> [1,0]"
%! assert(bucket([0,0.6,0],zero_one2,2) == [1,0])
%! assert(bucket([1,0.6,0],zero_one2,2) == [1,0])

%!test "d=2, p=2, [*,0,0.6] -> [0,1]"
%! assert(bucket([0,0,0.6],zero_one2,2) == [0,1])
%! assert(bucket([1,0,0.6],zero_one2,2) == [0,1])

%!test "d=2, p=2, [*,1,1] -> [1,1]"
%! assert(bucket([0,1,1],zero_one2,2) == [1,1])
%! assert(bucket([1,1,1],zero_one2,2) == [1,1])
