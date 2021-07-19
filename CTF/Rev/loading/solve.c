#include <stdio.h>

// Flag -> flag{f1v3_bi11i0n_y34r5_i_th1nk_th3_5un_is_r3d_gi4nt_n0w}
// Rewrote the exact code just reduced the time 

int main(){
    char flag[] = "\x30\x02\x04\x02\x1c\x5c\x56\x57\x5d\x63\x1f\x5d\x41\x1c\x58\x5b\x4f\x26\x54\x5b\x14\x54\x6e\x68\x25\x7f\x09\x42\x51\x01\x2c\x3b\x0d\x43\x54\x3a\x52\x13\x54\x70\x51\x50\x2e\x56\x1c\x0f\x66\x14\x06\x67\x5e\x13\x3c\x45\x49\x31\x02";
    char orz[] = "Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you";
    puts (flag);
    puts (orz);
    
    unsigned long i = 0;

    while (i < 0x25f839810977f55) {
        if (i%1000000 == 0){
            printf ("%ld\r", i);
            puts (flag);
        }
        flag[i % 0x39] = flag[i % 0x39] ^ orz[i % 0xab];
        // _flag.append({i%0x39:flag[i % 0x39] ^ orz[i % 0xab]})
        // # print("Loading flag")
        // local_18 = 0
        i = i + 1;
    }
    puts (flag);
    puts (orz);

    return 0;
}
