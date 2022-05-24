FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get -y update; apt-get -y install perl python3 build-essential openjdk-11-jdk git wget unzip
WORKDIR /gp
 
#ASPRAlign
RUN git clone https://github.com/bdslab/aspralign.git; \
 
    #PSMAlign
    wget http://homepage.cs.latrobe.edu.au/ypchen/psmalign/psmalign.tar.gz; \
    tar -xf psmalign.tar.gz; \
    rm psmalign.tar.gz; \
 
    #PSTAG
    wget http://pstag.dna.bio.keio.ac.jp/download/pstag2_1_2-unix.zip && unzip pstag2_1_2-unix.zip && rm pstag2_1_2-unix.zip; \
    cd pstag2_1_2-unix && chmod +x pstag && cd ..; \
 
    #RAG-2D
 
    #ViennaRNA
    wget https://www.tbi.univie.ac.at/RNA/download/sourcecode/2_5_x/ViennaRNA-2.5.0.tar.gz; \
    tar -xf ViennaRNA-2.5.0.tar.gz; \
    rm ViennaRNA-2.5.0.tar.gz; \
    cd ViennaRNA-2.5.0; \
    ./configure; \
    make; \
    make install; \
    cd ..; \
 
    #MiGaL
    wget http://www-igm.univ-mlv.fr/~allali/logiciels/migal_tgz/migal.tgz && tar -xf migal.tgz && rm migal.tgz; \
 
    #Gardenia
    wget https://bioinfo.lifl.fr/gardenia/gardenia.zip && unzip gardenia.zip && rm gardenia.zip; \
 
    #LocARNA
    wget https://github.com/s-will/LocARNA/releases/download/v2.0.0RC10/locarna-2.0.0RC10.tar.gz && tar -xf locarna-2.0.0RC10.tar.gz && rm locarna-2.0.0RC10.tar.gz; \
    cd locarna-2.0.0RC10; \
    ./configure; \
    make; \
    make install; \
    cd ..
 
ENV DISPLAY=host.docker.internal:0.0
 
ADD molecolePerTest ./molecolePerTest