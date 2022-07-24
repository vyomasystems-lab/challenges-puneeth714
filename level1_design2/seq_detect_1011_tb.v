`include "seq_detect_1011.v"
module seq_detect_1011_tb;
reg inp_bit,reset,clk;
wire seq_seen;
seq_detect_1011 s(seq_seen,inp_bit,reset,clk);
initial begin
    inp_bit = 0;
    clk=0;
    reset=1;
    #20 reset=0;
end
always #10 clk=~clk;
initial begin
    $dumpfile("seq_detect_1011_tb.vcd");
    $dumpvars(0,seq_detect_1011_tb);
    $monitor("inp = %b and seq_seen = %b and current %b next_state %b",inp_bit,seq_seen,s.current_state,s.next_state);
    #20 inp_bit = 0;
    #10 inp_bit = 1;
    #10 inp_bit = 0;
    #10 inp_bit = 1;
    #10 inp_bit = 1;

end
initial begin
    #100 $finish;
    end
endmodule