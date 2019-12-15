function out = isolated(img)
  notOnesIdx = find(img==0)
	nbr = nbrcount(img)
	zerosIdx = find(nbr==0)
	out = zeros(size(img))
	out(zerosIdx) = 1
	out(notOnesIdx) = 0
endfunction

%!test
%! A= [1,0,0; 0,0,0; 0,0,1; 1,0,0]
%! assert(isolated(A) == A)

%!test
%! A=[1,0,0;
%!    0,0,0;
%!    0,1,1;
%!    1,0,1];
%! assert(isolated(A) == [1,0,0; 0,0,0; 0,0,0;0,0,0])