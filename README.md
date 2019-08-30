## *I. BACKGROUND*

### A. Education: 
<img src="https://github.com/mtl-brainhack-school-2019/Nick-Hoang--Apply-BIDS-fMRIPrep-Nilearn-Jupiter-to-my-task-based-fMRI-data/raw/master/images/uoft%20psych%20logo.png" width=400>  <img src="https://github.com/mtl-brainhack-school-2019/Nick-Hoang--Preprocess-analyze-task-based-fMRI-data/raw/master/images/rotman%20logo.png" width=200>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I am an incoming Masters student in Psychology at the University of Toronto and Rotman Research Institute, Baycrest. 
  
### B. My research: 
       

* **Goal**: It is a task based fMRI study that tests 28 healthy young participants' long term memory recognition of highly similar scenes and correlate that with differential activation on the long-axis of the hippocampus (HPC) and neocrotical regions. 
    
* **Current** research: Neuroimaging research show that the posterior region of the hippocampus (Post-HPC) is associated with recollection of fine-grained local details; meanwhile the anterior region of the hippocampus (Ant-HPC) is associated with recollection of coarse global details.
 
* **Hypotheses**: We hypothesized that activation of the Post-HPC will be correlated with recognition accuracy of the many exemplars of a scene category, and the Ant-HPC will be correlated with recognition errors of generalizaing a scene category previously seen.
       
* **Methodology**: 
  * i. **Behavioural** - We use ePrime, a psychology presentation software, to present different exemplars of a scene        category, such as a bar, to participants at the Encoding (study phase) and then measure their recognition accuracy in responding "Old/Similar/New" to repeated, highly similar, and new scenes at Retrieval (test phase).
  
  <img src="https://github.com/mtl-brainhack-school-2019/Nick-Hoang--Apply-BIDS-fMRIPrep-Nilearn-Jupiter-to-my-task-based-fMRI-data/raw/master/images/SMST%20design%20imageB.png" width=800>
  
  * ii. **fMRI** - We use a Siemens Prisma 3T Scanner and our design comprise of 8 runs of Study1,Test1, Study2,Test2, Anatomical, Study3,Test3, Study4,Test4. We use SPM8 and MatLab to preprocess and analyze our data.
  
  <img src="https://github.com/mtl-brainhack-school-2019/Nick-Hoang--Apply-BIDS-fMRIPrep-Nilearn-Jupiter-to-my-task-based-fMRI-data/raw/master/images/fMRI%20task%20design.png"> 
                                  

## *II. BRAINHACK 2019*

### A. Dataset: 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I will use the DICOM data of one particpant from the above study.

### B. Tools: 
Tool          | Description
------------- | -------------
GitHub        | modify via push/pull files in my repository
BIDS          | organize my DICOMs
fMRIPrep      | Preprocess my data: slice timing, smoothing, spatial normalization
Nilearn       | HPC ROI and whole brain analyses
Jupyter       | Present my analyses and data visualization


### C. Deliverables: 
* Github repository of python scripts to run BIDS apps like fMRIPrep
* BOLD preprocessed data and images via fMRIPrep
* Jupyter notebook of whole brain and HPC ROI analyses via Nilearn
  
### D. Medium: 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I hope to use Jupyter to present my analyses and data visualization.

### E. To-Do list:
- [x] COMMIT TO ONE ENVIRONMENT: Conda in UBUNTU as vm in Win 10 Pro! :satisfied:
- [x] Learn to program with Python
- [x] Dcm2bids - convert dicoms to BIDS
- [x] Input study info into CONFIG file for BIDS
- [x] Dcm2niix - convert dicoms to nifti and json files
- [x] Heudiconv - alternative to dcm2bids
- [x] Onstall fMRIPrep via docker
- [x] Get CanadaCompute(CC) account (via temp sponsorship from Pierre :wink:)
- [x] Submit job via salloc on CC Beluga interactive node 
- [x] Submit job via sbatch on CC Beluga compute node 
- [ ] Submit job via salloc & sbatch on CC Cedar interactive & compute node respectively
- [ ] fMRIPrep preprocessing: get the html file per participant! 
- [ ] Use Nistats to do first and second level BOLD analyses 
- [x] Organize my csv data into dataframes via Pandas
- [x] Visualize my behavioral accuracy data via boxplots in Plotly-dash
- [x] Present my intro via Powtoon
- [x] Present my final results in Jupyter Notebook with Rise slideshow plugin
