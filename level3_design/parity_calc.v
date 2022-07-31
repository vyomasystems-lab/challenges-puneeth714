module parity_calc #(parameter WIDTH=10) (stream,clk,out);
    input [WIDTH-1:0] stream;
    input clk;
    output reg out;
    reg tmp=0;
    integer i;

    // check  the even parity of the stream and output the result
    always @(posedge clk)
    begin
        for(i=0;i<WIDTH;i=i+1)
        begin
            tmp=tmp;
        end
        out=tmp;
        tmp=0;
    end
endmodule
