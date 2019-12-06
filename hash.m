%This function takes a bucketed matrix and returns a single integer address from the bucket address

function out = hash(v, ranges, p)
  bucketed = bucket(v,ranges,p);
  sizeB = size(bucketed)(2);
  
  if(sizeB >= 2)
    pow = [0:sizeB];
    pow = p.^pow;
    
    out = dot(bucketed, pow(1:sizeB));
  else
    out = bucketed;
  endif
  out = out + 1;
  return
   
endfunction

%!test "[*,0] -> bucket 1"
%!shared zero_one
%! zero_one=[0,0;1,1];
%! assert(hash([0,0],zero_one,2) == 1)
%! assert(hash([1,0],zero_one,2) == 1)

%!test "[*,0.4] -> bucket 1"
%! assert(hash([0,0.4],zero_one,2) == 1)
%! assert(hash([1,0.4],zero_one,2) == 1)

%!test "[*,0.5] -> bucket 2"
%! assert(hash([0,0.5],zero_one,2) == 2)
%! assert(hash([1,0.5],zero_one,2) == 2)

%!test "[*,0.6] -> bucket 2"
%! assert(hash([0,0.6],zero_one,2) == 2)
%! assert(hash([1,0.6],zero_one,2) == 2)

%!test "[*,1] -> bucket 2"
%! assert(hash([0,1],zero_one,2) == 2)
%! assert(hash([1,1],zero_one,2) == 2)


%!test "[*,1] p=3 -> bucket 3"
%! assert(hash([0,1],zero_one,3) == 3)
%! assert(hash([1,1],zero_one,3) == 3)

%!test "[*,1] (range=1,2) -> bucket 1"
%!shared one_two
%! one_two=[1,1;2,2];
%! assert(hash([0,1],one_two,2) == 1)
%! assert(hash([1,1],one_two,2) == 1)

%!test "[*,1.5] (range=1,2, p=3) -> bucket 2"
%! assert(hash([0,1.5],one_two,3) == 2)
%! assert(hash([1,1.5],one_two,3) == 2)

%!test "d=2, p=2, [*,0,0] -> 1"
%!shared zero_one2
%! zero_one2=[0,0,0;1,1,1];
%! assert(hash([0,0,0],zero_one2,2) == 1)
%! assert(hash([1,0,0],zero_one2,2) == 1)

%!test "d=2, p=2, [*,0.6,0] -> 2"
%! assert(hash([0,0.6,0],zero_one2,2) == 2)
%! assert(hash([1,0.6,0],zero_one2,2) == 2)

%!test "d=2, p=2, [*,0,0.6] -> 3"
%! assert(hash([0,0,0.6],zero_one2,2) == 3)
%! assert(hash([1,0,0.6],zero_one2,2) == 3)

%!test "d=2, p=2, [*,1,1] -> 4"
%! assert(hash([0,1,1],zero_one2,2) == 4)
%! assert(hash([1,1,1],zero_one2,2) == 4)

%!test "extra"
%! assert(hash([0,1,1, 5, 5, 7], [0,0,0,0,0;,7,7,7,7,7],2) == 4)
%! assert(hash([1, 7.2, 4, 7.3, 3.2], [0,0,0,0,0;,7,7,7,7,7],2) == 4)
