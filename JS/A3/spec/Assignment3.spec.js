let ms = require("../Assignment3.js");

    describe("flatten",
     function () {
         it("base case",
        function () {
            expect(ms.flatten([])).toEqual([]);
        });
         it("single element",
        function () {
            expect(ms.flatten([1])).toEqual([1]);
            expect(ms.flatten(["foo"])).toEqual(["foo"]);
            expect(ms.flatten([{foo: 1}])).toEqual([{foo: 1}]);                     
        });
         it("longer list, no mutation",
        function () {
            var data = [[[1],2,[3]],4,[5,6]];
            var orig_data = data;
            expect(ms.flatten(data)).toEqual([1,2,3,4,5,6]);
            expect(data).toEqual(orig_data);
        });
     });

     describe("summarize_mail",
     function() {
         it("no headers",
        function () {
            expect(ms.summarize_mail("example1.json")).toEqual([{}, {}, {}]);
            expect(ms.summarize_mail("example2.json")).toEqual(Array(10).fill({}));
        });
         it("Subject",
        function () {
            expect(ms.summarize_mail("example1.json",'Subject')).toEqual([{Subject: "[notmuch] archive"},
                                          {Subject: "Re: [notmuch] archive"},
                                          {Subject: "Re: [notmuch] archive"}]);
        });
         it("Subject, Date",
        function () {
            expect(ms.summarize_mail("example1.json",'Subject','Date')).toEqual(
            [{Subject: "[notmuch] archive", Date: 'Tue, 17 Nov 2009 18:21:38 -0500'},
             {Subject: "Re: [notmuch] archive", Date: 'Tue, 17 Nov 2009 18:04:31 -0800'},
             {Subject: "Re: [notmuch] archive", Date: 'Wed, 18 Nov 2009 02:22:12 -0800'}]);
        });
     });

let testMsg = new Message({'headers': {'Subject' : "lunch", 'Date' : "now"}});
describe("Message class",
         function() {
             it("new message is not null",
                function () {
                    expect(testMsg).not.toEqual(null);
                });
             it("subject accessor",
                function () {
                    expect(testMsg.subject).toEqual("lunch");
                });
         });

let otherMsg = new Message({'headers': {'Subject' : "dinner", 'Date' : "now"}});
it("message is equal to itself",
   function () {
       expect(testMsg.equals(testMsg)).toEqual(true);
   });
it("message is not equal if field changes",
   function () {
       expect(testMsg.equals(otherMsg)).toEqual(false);
   });