##usage: matrix = percent(raw, maxes)
##
## raw - raw scores, one row per student.
## maxes - maximum possible for that column
##
## Output is a matrix one row per student, with ratios
function out=normalize(raw, maxes)
 out = raw./maxes
endfunction
%!test
%! #    journal,assgn,  midterm,final
%! mxs=[260,    60,     20,     60];
%! nrm = [0.9, 0.9, 0.9, 0.9; 0.75, 0.75, 0.75, 0.75; 1, 0, 1, 0];
%! raw=[234, 54, 18, 54; 195, 45, 15, 45; 260, 0, 20, 0];

%! assert(normalize(raw, mxs), nrm, eps);