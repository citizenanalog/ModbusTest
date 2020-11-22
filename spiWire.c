#include <wiringPiSPI.h>
//#include <stdint.h>
//#include <unistd.h>
//#include <stdio.h>
//#include <stdlib.h>
//#include <getopt.h>
//#include <fcntl.h>
//#include <sys/ioctl.h>
//#include <linux/types.h>
//#include <linux/spi/spidev.h>
//#include <sys/mman.h>


int main(int argc, char *argv[])
{
  wiringPiSetup () ;
  pinMode (7, OUTPUT) ;

  for (;;)
  {
    digitalWrite (7, HIGH) ; delay (500) ;
    digitalWrite (7,  LOW) ; delay (500) ;
  }
  return 0 ;

}
