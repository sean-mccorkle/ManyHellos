FROM kbase/kbase:sdkbase.latest
MAINTAINER KBase Developer
# -----------------------------------------

# Insert apt-get instructions here to install
# any required dependencies for your module.

# RUN apt-get update

# taking a shot in the dark here: deploy njs_wrapper from /kb/dev_container?

RUN \
  . /kb/dev_container/user-env.sh && \
  cd /kb/dev_container/modules && \
  rm -rf jars && \
  git clone https://github.com/kbase/jars && \
  rm -rf kb_sdk && \
  git clone https://github.com/kbase/kb_sdk -b develop && \
  rm -rf handle_service && \
  git clone https://github.com/kbase/handle_service && \
  cd /kb/dev_container/modules/jars && \
  make deploy && \
  cd /kb/dev_container/modules/kb_sdk && \
  make && make deploy && \
  cd /kb/dev_container/modules/handle_service && \
  make && make deploy 

RUN echo building njs wrapper anew && \
    cd /kb/dev_container/modules && \
    rm -rf njs_wrapper && \
    git clone https://github.com/kbase/njs_wrapper && \
    cd njs_wrapper && \
    git checkout develop && \
    . /kb/dev_container/user-env.sh && \
    rsync -avp /kb/dev_container/modules/njs_wrapper/lib/biokbase/njs_wrapper/ /kb/deployment/lib/biokbase/njs_wrapper/
    # cd /kb/dev_container/modules/njs_wrapper && make && make TARGET=/kb/deployment deploy && cd ../../.. 

# -----------------------------------------

COPY ./ /kb/module
RUN mkdir -p /kb/module/work
RUN chmod 777 /kb/module

WORKDIR /kb/module

RUN make all

ENTRYPOINT [ "./scripts/entrypoint.sh" ]

CMD [ ]
